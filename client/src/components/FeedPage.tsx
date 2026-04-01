// FeedPage.tsx
import PostCard from "./PostCard";
import { Box, CircularProgress, Typography, Container } from "@mui/material";
import { useCallback, useEffect, useState, useRef } from 'react';
import { vkGetPosts } from '../api/api';
import { useInfiniteScroll } from "../hooks/useInfiniteScroll";

interface Publisher {
  name: string;
  photo_url: string;
}

interface FeedPost {
  publisher: Publisher;
  likes: number;
  reposts: number;
  views: number;
  timestamp: number;
  is_pinned: boolean;
  text: string;
  photos_url: string[] | null;
}

export const FeedPage: React.FC = () => {
  const [posts, setPosts] = useState<FeedPost[]>([]);
  const [hasMore, setHasMore] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  
  const POSTS_PER_PAGE = 5;
  const loadingRef = useRef(false);

  const loadPosts = useCallback(async () => {
    if (loadingRef.current || !hasMore) return;
    
    loadingRef.current = true;
    setIsLoading(true);
    setError(null);
    
    try {

      const currentOffset = posts.length; // кол-во загруженных постов
      
      const newPosts = await vkGetPosts('elitesos', POSTS_PER_PAGE, currentOffset);
      
      if (!newPosts || !Array.isArray(newPosts)) {
        throw new Error('Неверный формат ответа от сервера');
      }
      
      if (newPosts.length === 0) {
        setHasMore(false);
      } else {
        setPosts(prev => [...prev, ...newPosts]);
      }
    } catch (err: any) {
      console.error('Ошибка:', err);
      setError(err.message || 'Не удалось загрузить посты');
      setHasMore(false);
    } finally {
      setIsLoading(false);
      loadingRef.current = false;
    }
  }, [posts.length, hasMore]);

  const { lastElementRef } = useInfiniteScroll({
    hasMore,
    isLoading,
    onLoadMore: loadPosts
  });

  useEffect(() => {
    if (posts.length === 0 && !isLoading) {
      loadPosts();
    }
  }, []);

  if (error && posts.length === 0) {
    return (
      <Container maxWidth="md" sx={{ py: 4 }}>
        <Box sx={{ textAlign: 'center' }}>
          <Typography variant="h6" color="error" gutterBottom>
            Ошибка загрузки
          </Typography>
          <Typography color="text.secondary">{error}</Typography>
        </Box>
      </Container>
    );
  }

  return (
    <Container maxWidth="md" sx={{ py: { xs: 2, sm: 3, md: 4 } }}>
      <Box sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center',
        gap: 2 
      }}>
        {posts.map((post, index) => (
          <div
            key={post.timestamp}
            // реф вешается только на последний пост
            ref={index === posts.length - 1 ? lastElementRef : null}
            style={{ width: '100%', maxWidth: 600 }}
          >
            <PostCard 
              timestamp={post.timestamp}
              text={post.text}
              imageUrl={post.photos_url?.[0]}
              publisherName={post.publisher.name}
              publisherAvatar={post.publisher.photo_url}
              sourceAvatar={post.publisher.photo_url}
            />
          </div>
        ))}
        
        {isLoading && (
          <Box sx={{ display: 'flex', justifyContent: 'center', py: 2 }}>
            <CircularProgress size={40} sx={{ color: '#8B8B8B' }} />
          </Box>
        )}
        
        {!hasMore && posts.length > 0 && (
          <Typography sx={{ color: '#8B8B8B', py: 2, textAlign: 'center' }}>
            Вы посмотрели все посты
          </Typography>
        )}
      </Box>
    </Container>
  );
};

export default FeedPage;
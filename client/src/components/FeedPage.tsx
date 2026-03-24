import PostCard from "./PostCard";
import { Box } from "@mui/material";
import { Grid, Container } from "@mui/material";
import { useEffect, useState } from 'react';
import {vkGetPosts } from '../api/api';

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
  const [posts, setPosts] = useState<FeedPost[]>([])

  useEffect(() => {
    vkGetPosts('elitesos', 10).then(setPosts).catch(console.error)
  }, [])

  return (
    <Container maxWidth="md" sx={{ py: { xs: 2, sm: 3, md: 4 } }}>
      <Box sx={{ 
        display: 'flex', 
        flexDirection: 'column', 
        alignItems: 'center',
        gap: 2 
      }}>
        {posts.map((post) => (
          <PostCard 
            key={post.timestamp}
            timestamp={post.timestamp}
            text={post.text}
            imageUrl={post.photos_url?.[0]}
            publisherName={post.publisher.name}
            publisherAvatar={post.publisher.photo_url}
            //  sourceAvatar={post.sourceAvatar}

          />
        ))}
      </Box>
    </Container>
  )

}

export default FeedPage;

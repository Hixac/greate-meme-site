import { useCallback, useRef } from 'react';

interface UseInfiniteScrollProps {
  hasMore: boolean;
  isLoading: boolean;
  onLoadMore: () => void;
}

export const useInfiniteScroll = ({
  hasMore,
  isLoading,
  onLoadMore
}: UseInfiniteScrollProps) => {
  const observerRef = useRef<IntersectionObserver | null>(null);

  const lastElementRef = useCallback((node: HTMLDivElement | null) => {
    if (isLoading) return;

    // если уже есть наблюдатель — отключаем
    // т.к если элемент меняется старый observer должен перестать следить
    if (observerRef.current) {
      observerRef.current.disconnect();
    }

    observerRef.current = new IntersectionObserver(
      (entries) => {
        // entries[0] — наблюдаемый элемент
        // isIntersecting — true когда он появляется в зоне видимости
        // hasMore — есть ли еще посты для загрузки
        if (entries[0].isIntersecting && hasMore) {
          onLoadMore();
        }
      },
      { 
        threshold: 0.1,
        rootMargin: '400px' 
      }
    );

    if (node) {
      observerRef.current.observe(node);
    }
  }, [isLoading, hasMore, onLoadMore]);
  return {lastElementRef};

};
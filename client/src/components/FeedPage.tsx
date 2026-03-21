import PostCard from "./PostCard";
import { Box } from "@mui/material";
export default function FeedPage() {
  return (
    <>
    <Box component="section" sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
      <PostCard/>
    </Box>
      
    </>
  )

}


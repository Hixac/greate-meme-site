import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import { Box, Typography, CardContent } from '@mui/material';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import ExpandableText from './ExpandableText';

interface MemePost {
  timestamp: number;
  sourceAvatar: string; // сурс - источник на котором расположен ориг пост
  publisherAvatar: string;  // паблишер - паблик/канал ориг поста
  publisherName: string;
  imageUrl?: string | null;
  text: string;

}

const PostCard: React.FC<MemePost> = ({ 
  sourceAvatar, 
  publisherAvatar, 
  publisherName, 
  imageUrl, 
  text 
}) => {
  return (
    <Card 
      sx={{ 
        width: '100%',
        maxWidth: 600,
        height: 'auto', 
        p: { xs: 1, sm: 2 },
        background: '#282828', 
        color: 'white', 
        borderRadius: { xs: 1, sm: 2 },
        display: 'flex', 
        flexDirection: 'column'
      }}
    >
      <CardHeader 
        sx={{  
          p: { xs: 1, sm: 2 }
        }}
        avatar={
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
            <Avatar 
              sx={{ 
                borderRadius: 15, 
                width: { xs: 20, sm: 25 }, 
                height: { xs: 20, sm: 25 } 
              }} 
              src={sourceAvatar}
            />
            <Avatar 
              sx={{ 
                borderRadius: 15, 
                width: { xs: 35, sm: 40 }, 
                height: { xs: 35, sm: 40 } 
              }} 
              src={publisherAvatar}
            />
          </Box>
        }
        title={
          <Typography sx={{ 
            fontSize: { xs: 13, sm: 15 },
            fontWeight: 500
          }}>
            {publisherName}
          </Typography>
        }
        action={
          <IconButton aria-label="settings">
            <MoreHorizIcon sx={{ 
              width: { xs: 18, sm: 20 }, 
              height: 'auto', 
              color: '#8B8B8B' 
            }}/>
          </IconButton>
        }
      />
      
      {imageUrl && (
        <CardMedia
          component="img"
          sx={{
            width: '100%',
            height: 'auto',
            objectFit: 'cover',

          }}
          image={imageUrl}
          alt="post photo"
        />
      )}
      
      <CardContent sx={{ 
        p: { xs: 1, sm: 2 },
        '&:last-child': { pb: { xs: 1, sm: 2 } } 
      }}>
        <ExpandableText text={text} maxLength={100} />
      </CardContent>
    </Card>
  );
}

export default PostCard;
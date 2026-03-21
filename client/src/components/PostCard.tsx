import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardMedia from '@mui/material/CardMedia';
import Avatar from '@mui/material/Avatar';
import IconButton from '@mui/material/IconButton';
import { Box, Typography, CardContent } from '@mui/material';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';

export default function PostCard() {
  return (
    <Card className='card-container' sx={{ width: '40%', height: 'auto', p: 2, background: '#282828', color: 'white', borderRadius: 1, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
      <CardHeader sx={{width: '100%'}}
        avatar={
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
          <Avatar sx={{borderRadius: 15, width:40, height:40 }} src='https://avatars.mds.yandex.net/i?id=e17cd909cdf0c378c4865529882da8bb_l-6974550-images-thumbs&n=13'/>
          <Avatar sx={{borderRadius: 15, width:80, height:80 }} src='https://sun9-53.userapi.com/s/v1/ig2/Qgpm4H8mL4oAKj6oCxNKp_c9IatDc9lTbH25k6Ip0Diw_PIa_IWc9bKtAtKZGZhivHHnVAtSGzodM-yU44Y8cKSr.jpg?quality=95&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,720x1080,1080x1620,1280x1920,1440x2160,1707x2560&from=bu&cs=1280x0'/>
          </Box>
        }
        title={
          <Typography sx={{fontSize: 20}}>
            Shrimp and Chorizo Paella
          </Typography>
        }
        action={
          <IconButton aria-label="settings" >
            <MoreHorizIcon sx={{width: 40, height: 'auto', color: '#8B8B8B'}}/>
          </IconButton>
        }
      >
      </CardHeader>
      <CardMedia
        component="img"
        height="auto"
        image="https://sun9-26.userapi.com/s/v1/ig2/0Wvr_JJ8PmzH7qAPnsQ5jHECmc06e7kC2hEmpKDlg7rPfhQ_IgyVc3vyGfmTS89O_oal_LvkedzhZItRRAKfZtGs.jpg?quality=96&as=32x24,48x35,72x53,108x79,160x118,240x177,360x265,480x353,540x397,640x471,720x530,947x697&from=bu&u=_HDV_1QSBMYvA0nAmCd5GrEC5w9-9w2qowySJSv8-dI&cs=947x0"
        alt="Paella dish"
      />
      <CardContent>
        <Typography variant="body1" sx={{ color: 'white' }}>
          Lizards are a widespread group of squamate reptiles, with over 6,000
          species, ranging across all continents except Antarctica
        </Typography>
      </CardContent>
    </Card>
  );
}

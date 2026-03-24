import React, { useState } from 'react';
import { Box, Typography } from '@mui/material';

interface ExpandableTextProps {
  text: string;
  maxLength?: number;
}

const ExpandableText: React.FC<ExpandableTextProps> = ({ text, maxLength = 100 }) => {
  const [expanded, setExpanded] = useState(false);
  const needTruncate = text.length > maxLength;

  const truncatedText = `${text.slice(0, maxLength)}...`;

  const handleTextClick = () => {
    if (needTruncate) {
      setExpanded(!expanded);
    }
  };

  return (
    <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
      <Box sx={{ flex: 1 }}>
        <Typography
          variant="body1"
          sx={{
            wordBreak: 'break-word',
            cursor: needTruncate ? 'pointer' : 'default',
            fontSize: { xs: 14, sm: 16 },
            lineHeight: { xs: 1.3, sm: 1.5 }
          }}
          onClick={handleTextClick}
        >
          {needTruncate && !expanded ? truncatedText : text}
        </Typography>
      </Box>
    </Box>
  );
};

export default ExpandableText;
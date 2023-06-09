import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';

export function Copyright(props) {
    return (
      <Typography variant="body2" color="text.secondary" align="center" {...props}>
        {'Copyright © '}
        {/* TODO: add a link */}
        <Link color="inherit" href="#">
          Business HQ
        </Link>{' '}
        {new Date().getFullYear()}
        {'.'}
      </Typography>
    );
  }
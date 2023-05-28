import React from "react";
import { 
  Link, 
  // withRouter 
} from "react-router-dom";
import { route_links as links } from "../../routes/main";

import AppBar from "@mui/material/AppBar";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
// import { Link as MuiLink } from '@mui/material/Link';
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardHeader from "@mui/material/CardHeader";
import StarIcon from "@mui/icons-material/StarBorder";
import Toolbar from "@mui/material/Toolbar";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import GlobalStyles from "@mui/material/GlobalStyles";
import { styled } from "@mui/material/styles";


function Hero() {
  
  // styles for nav links
  const StyledLink = styled(Link)`
  color: #6c6c6c;
  text-decoration: none;
  margin: 1rem;
  position: relative;

  &:hover {
    color: #c1c1c1;
    text-decoration: none;
  }

  ${(props) =>
    props.disabled &&
    `
    pointer-events: none;
    color: LightGrey;
    text-decoration: underline;
  `}
`;


  return (
    <div>
      <CssBaseline />
      <AppBar
        position="static"
        color="default"
        elevation={0}
        sx={{ borderBottom: (theme) => `1px solid ${theme.palette.divider}` }}
      >
        <Toolbar sx={{ flexWrap: "wrap" }}>
          <Typography variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
            {/* TODO: add a company logo in svg */}
            Company name
          </Typography>

          <nav>
            <StyledLink to={links.home} disabled={location.pathname === links.home}>Home</StyledLink>
            <StyledLink to={links.services_catalogue} disabled={location.pathname === links.services_catalogue}>Catalogue</StyledLink>
            <StyledLink to={links.contact} disabled={location.pathname === links.contact}>Contact</StyledLink>
            <StyledLink to={links.portfolio} disabled={location.pathname === links.portfolio}>Portfolio</StyledLink>
          </nav>

          <Button
            href={links.login_customer}
            variant="outlined"
            sx={{ my: 1, mx: 1.5 }}
          >
            Login
          </Button>

        </Toolbar>
      </AppBar>
    </div>
  );
}
// TODO: refresh link style with route load
// const MyComponentWithRouter = withRouter(MyComponent);

export default Hero;

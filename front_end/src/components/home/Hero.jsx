import React from "react";
import { useRef } from "react";
import { 
  Link, NavLink, 
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


function ActiveNavLink(isActive) {
  /*styling for navigation links*/
  return isActive ? {
    color: "#00aae1",
    backgroundColor: "#00c9ff33",
    padding: "5px",
    borderRadius: "5px",
    fontWeight: 700,
  } : 
  {
    color: "#6c6c6c",
    textDecoration: null,
    margin: "1rem",
    position: "relative",
    fontWeight: 700,
  }
  
}

function Hero() {
  
  // styles for nav links
  const StyledLink = styled(Link)`
  color: #6c6c6c;
  text-decoration: none;
  margin: 1rem;
  position: relative;
  font-weight: 700;

  &:hover {
    color: #c1c1c1;
    text-decoration: none;
  }

  ${(props) =>
    props.disabled &&
    `
    pointer-events: none;
    color: #00aae1;
    background-color: #00c9ff33;
    padding: 5px;
    border-radius: 5px;
  `}
`;

    let current_url = window.location.pathname

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
            <img src="/home/BHQ_logo.png" className='nav-logo-image'/>
          </Typography>

          {/* TODO: disable nav links if they lead to the current page */}
          <nav>
            <StyledLink 
              to={links.home} 
              disabled={current_url === links.home}
              className="nav-links" reloadDocument>
              Home
            </StyledLink>
            <StyledLink 
              to={links.services_catalogue} 
              disabled={current_url === links.services_catalogue}
              className="nav-links" reloadDocument>
              Catalogue
            </StyledLink>
            <StyledLink 
              to={links.contact} 
              disabled={current_url === links.contact}
              className="nav-links" reloadDocument>
              Contact
            </StyledLink>
            <StyledLink 
              to={links.portfolio} 
              disabled={current_url === links.portfolio}
              className="nav-links" reloadDocument>
              Portfolio
            </StyledLink>
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

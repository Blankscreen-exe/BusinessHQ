import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'

// importing componenets
import Login from './components/login/index'
import SignUp from './components/login/SignUp'
import StaffLogin from './components/login/StaffLogin'
import Services from './components/services'
import Catalogue from './components/services/Catalogue'
import Portfolio from './components/portfolio'
import Contact from './components/contact'
import Home from './components/home'
import Hero from './components/home/Hero'
import Footer from './components/home/Footer'
// import Dashboard from './components/analytics/Dashboard'

// importing route constants
import { route_links as link } from './routes/main'

function App() {
  
  console.log("RUNNING FROM APP ",window.location.pathname)

  // UI resources

  // https://mui.com/material-ui/getting-started/templates/
  
  // https://reactrouter.com/en/main/start/tutorial

  return (
    <>
      {/* navbar */}
      <Hero/>

      {/* routes to different sections */}
      <Routes>
        <Route 
          path={link.home} 
          element={<Home/>}
          />
        <Route 
          path={link.login_customer} 
          element={<Login/>}
          />
        <Route 
          path={link.register_customer} 
          element={<SignUp/>}
          />
        <Route 
          path={link.login_staff} 
          element={<StaffLogin/>}
          />
        <Route 
          path={link.services_catalogue} 
          element={<Catalogue/>}
          />
        <Route 
          path={link.portfolio} 
          element={<Portfolio/>}
          />
        <Route 
          path={link.contact} 
          element={<Contact/>}
          />
      </Routes> 

      <Footer/>
    </>
  )
}

export default App

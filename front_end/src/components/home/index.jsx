import React from 'react'

import Footer from './Footer'
import Services from '../services'
import Login from '../login'
import Hero from './Hero'


function Home() {
  return (
    <div className='home-container'>Home

<Hero/>
<Services/>
<Login/>
<Footer/>
    </div>
  )
}

export default Home
import React from 'react'

function Notfound() {
  return (
    <>
      <img src="/notfound/notfound.jpg" className='not-found-404'/>
      <h1 align="center" className='not-found-title blue'> 404 Not found </h1>
      <p className='not-found-message gray'>Sorry about that .. but looks like the page you were looking for does not exist.</p>
    </>
  )
}

export default Notfound
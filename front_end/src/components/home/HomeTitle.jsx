import React from 'react'

const wallpaper_styles = {
    maxWidth: "50%",
    minWidth: "350px",
    maxHeight: "350px",
    borderRadius: "10px",

}

function HomeTitle() {

  return (
    <div className="flex-center">
        <img id='Home_Title'/>
        <h2 className='title-font'>
            Your Personal <span className="golden-font">Business Platform</span>
        </h2>
        <img src="/home/main_wallpaper.png" className='home-wallpaper'/>
        <h2>Grow Your Potential!</h2>
    </div>
  )
}

export default HomeTitle
import React from 'react'
import StaffLogin from './StaffLogin'
import CustomerLogin from './CustomerLogin'
import SignUp from './SignUp'


export default function Login() {
  return (
    <div>Login
        {/* TODO: do some logic here */}
  console.log(window.location.pathname)

        <CustomerLogin/>
    </div>
  )
}

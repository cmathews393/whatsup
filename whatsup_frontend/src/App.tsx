import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

function getMonitors() {
  fetch('/api/v1/monitors')
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error('Error fetching monitors:', error);
    });
}

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <button onClick={getMonitors}>Get Monitors</button>

        <div className="card">
          <h1>Welcome to Whatsup!</h1>
          <p>Whatsup is a scheduling app that allows you to schedule messages to be sent to your friends and family at a later time.</p>
          <img src={heroImg} alt="Hero Image" className="hero-image" />
        </div>
      </div>
    </>
  )
}

export default App

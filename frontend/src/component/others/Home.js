
import React,{useEffect} from 'react'

const Home = ({setProgress}) => {

  useEffect(() => {
    setProgress(40)

    setTimeout(() => {
      setProgress(100)
    }, 1000)
    // eslint-disable-next-line
  }, [])

  return (
    <div className='main-section-container'>
      
    </div>
  )
}

export default Home

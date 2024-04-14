import React, { useState,useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

const Login = ({setProgress}) => {

    const [credentials, setCredentials] = useState({ email: "", password: "" })

    useEffect(() => {
        setProgress(40)
    
        setTimeout(() => {
          setProgress(100)
        }, 1000)
        // eslint-disable-next-line
      }, [])

    let history = useNavigate()
    const handleSubmit = async (e) => {
        try {
            e.preventDefault()
            let host = process.env.REACT_APP_HOST;
            const response = await fetch(`${host}/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email: credentials.email, password: credentials.password })
            })
            const json = await response.json()
            if (json.success) {
                // localStorage.setItem('token',json.authToken)
                // localStorage.setItem('email',json.userCode)

                let First_Name = json.data_list[0].First_Name
                let Last_Name = json.data_list[0].Last_Name
                let Full_Name = First_Name + ' ' + Last_Name

                localStorage.setItem('auth-Token',json.message)
                localStorage.setItem('Full_Name',Full_Name)
                localStorage.setItem('User_Code',json.data_list[0].User_Code)
                history('/')
                //console.log(json.message)
            }
        }
        catch (error) {
            throw error
        }

    }

    const onChange = (e) => {
        setCredentials({ ...credentials, [e.target.name]: e.target.value })
    }
    return (
        <div className="container-sm ">
            <div className='row justify-content-md-center'>
                <div className="col">

                </div>
                <div className='col'>
                    <form >
                        <div className="mb-3">
                            <label htmlFor="email" className="form-label">Email address</label>
                            <input type="email" className="form-control" id="email" name="email" aria-describedby="emailHelp" onChange={onChange} value={credentials.email} />
                        </div>
                        <div className="mb-3">
                            <label htmlFor="password" className="form-label">Password</label>
                            <input type="password" className="form-control" id="password" name="password" onChange={onChange} value={credentials.password} />
                        </div>
                        <button type="submit" className="btn btn-primary" onClick={handleSubmit}>Submit</button>
                    </form>
                </div>

                <div className='col'>

                </div>
            </div>

        </div>

    )
}

export default Login

import React from 'react'

export default function Module_FirstPage(props) {
    return (
        <div className="left-content">
            <div className="desc-container">
                <div className="heading">
                    <h1 className='mx-2'>{props.Title}</h1>
                </div>
                <div>
                {localStorage.getItem('auth-Token') ? <button className="btn btn-outline-primary mx-3" id="Update" onClick={props.Onclick}>Update List</button> :<div></div>}
                </div>
            </div>
        </div>

    )
}

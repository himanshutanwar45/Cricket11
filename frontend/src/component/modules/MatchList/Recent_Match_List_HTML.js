import React, { useContext, useEffect } from 'react'
import ModuleFirstPage from '../../others/ModuleFirstPage'
import noteContext from '../../../contexts/notes/NoteContext'
import { useNavigate } from 'react-router-dom'

export default function Recent_Match_List_HTML({ setProgress, showAlert }) {

    const contexts = useContext(noteContext)

    const { notes, GetMatchType, GetRecentMatchList, matchList } = contexts

    let history = useNavigate();

    useEffect(() => {
        setProgress(40)
        setTimeout(() => {
            GetMatchType(); 
            GetRecentMatchList('International')
            setProgress(100)
        }, 1000)


        setTimeout(()=>{
            cssClass("International")
        },1500);

        // eslint-disable-next-line
    }, [])

    const handledAPICall = () => {
        showAlert('Clicked', 'success')
    }

    const handledClickonTab = async (Item) => {
        try {
            cssClass(Item)
            GetRecentMatchList(Item)
        } catch (error) {
            throw error
        }

    }

    const cssClass = (Item) => {
        try {
            const tabs = document.querySelectorAll('.tabs-header-content-text-matchList');
            tabs.forEach(tab => {
                tab.classList.remove('active');
            });
            
            const clickedTab = document.getElementById(`tab-header-span-${Item}`);
            if (clickedTab) { 
                clickedTab.classList.add('active');
            } else {
                throw new Error(`Element with ID 'tab-header-span-${Item}' not found`);
            }
    
        } catch (error) {
            throw error;
        }
    }

    return (
        <div className="main-section-container">
            <ModuleFirstPage Title="Recent Match List" Onclick={handledAPICall}></ModuleFirstPage>
            <div className="right-content">
                <div className="tabs-container-matchList">
                    <div className="tabs-header-matchList" id="tab-header">
                        {notes.map((item, index) => (
                            <div className={`tabs-header-content-matchList`} key={index}><span className="tabs-header-content-text-matchList" id={`tab-header-span-${item.Match_Type}`} style={{'cursor':'pointer'}} onClick={() => { handledClickonTab(item.Match_Type) }}>{item.Match_Type}</span></div>
                        ))}
                    </div>
                    <div className="packs-card-container-matchList" id="packs-card-container">
                        {matchList.length === 0 && 'No match to display'}
                        {matchList.map((item, index) => (
                            <div className="pack-card-content-matchList" key={index}>
                                <div className="pack-card-left-section-matchList">
                                    <div className="pack-card-details-matchList">
                                        <div className="pack-card-detail-matchList">
                                            <h5 className="pack-card-heading-matchList"> {item.Start_Date}  </h5>
                                        </div>
                                        <div className="pack-card-detail-matchList">
                                            <h5 className="pack-card-heading-matchList">  {item.Series_Name}  </h5>
                                        </div>

                                        <div className="pack-card-detail-matchList">
                                            <h5 className="pack-card-heading-matchList">Runs: <strong>{item.Runs}</strong> </h5>
                                        </div>
                                    </div>
                                    <div className="pack-card-benefits-heading">{item.Match_Format}</div>
                                    <br></br>
                                    <div className="pack-card-benefits-heading">{item.City} ({item.Ground}) </div>
                                </div>
                                <div className="pack-card-right-section">
                                    <button className="btn btn-outline-danger mx-2" id={`button-${item.Match_Id}`} onClick={() => history({pathname:`/get_recentMatch/get_score/${item.Match_Id}`,
                                                                                                                        state:{teamId:item.Match_Id}})} >GET</button>
                                </div>

                                {/* <div className="pack-card-right-section">
                                    <button className="btn btn-outline-danger mx-2" id={`API-${item.Team_Id}`} >+</button>
                                </div> */}
                            </div>
                        ))}
                    </div>
                </div>

            </div>
        </div>
    )
}

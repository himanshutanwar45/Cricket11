import React, { useState } from "react";
import NoteContext from "./NoteContext";
import {Get_Team_Data,GetPlayerData,GetPlayerDetails,GetTeamName,GetPlayerName} from '../../JS_Data/TeamList_Module/GetTeamData'
import {Get_Team_Data_API,Get_TeamPlayer_By_Id_API,Get_TeamPlayer_By_PlayerId_API} from '../../JS_Data/aPIs/TeamList/TeamAPI'
import {Get_Match_Type,Get_Recent_Match,Get_Recent_Match_Score,Get_Recent_Match_Score_Batter, Get_Recent_Match_Score_Bowler} from '../../JS_Data/MatchList_Module/GetMatchListData'

const NoteState = (props) => {
  const [notes, setNotes] = useState([]);

  const [matchList, setMatchList] = useState([])

  const [teamName ,setTeamName] = useState(['Not Found'])

  ////////////////////// Start of Team List /////////////////////////////////////////////////////////////////

  // Function to fetch team list
  const GetTeamList = async (teamType) => {
    try {
      setNotes([])
      const response = await Get_Team_Data(teamType);
      setNotes(response);
    } catch (error) {
      //console.error("Error fetching team list:", error);
      throw error
    }
  };

  // Function to fetch team player list (GET)
  const GetTeamPlayerList = async (teamId) => {
    try {
      setNotes([])
      const response = await GetPlayerData(teamId);
      setNotes(response);
    } catch (error) {
      console.error("Error fetching team player list:", error);
      throw error
    }
  };

  // Function to fetch team player list
  const GetPlayerDetailsList = async (playerId,teamId) => {
    try {
      setNotes([])
      const response = await GetPlayerDetails(playerId,teamId);
      setNotes(response);
    } catch (error) {
      console.error("Error fetching team player list:", error);
      throw error
    }
  };

  //Function to fetch the team name from team id

  const GetTeamNameId = async (teamId) =>{
    try{
      
      setTeamName([])
      const response = await GetTeamName(teamId)
      setTeamName(response)

    }catch(error){
      throw error
    }
  }

  //Function to fetch the Player name from player id

  const GetPlayerNameId = async (playerId,teamId) =>{
    try{
      
      setTeamName([])
      const response = await GetPlayerName(playerId,teamId)
      setTeamName(response)

    }catch(error){
      throw error
    }
  }

  ///////////////////////////////// API Calling /////////////////////////////////////////////////////////////////////////////////////
  //Functionn to call the Team list api from cricbuzz (rapidapi)

  const GetTeamListAPI  = async () => {
    try{
      const response = await Get_Team_Data_API();
      return response
    }
    catch(error){
      throw error
    }
  }


  //Functionn to call the Player List by Team Id api from cricbuzz (rapidapi)
  const GetPlayerByTeamIdAPI = async (teamId) =>{
    try{
      const response = await Get_TeamPlayer_By_Id_API(teamId)
      return response

    } catch(error){
      throw error
    }
  }


  //Functionn to call the Player Info by Player Id api from cricbuzz (rapidapi)
  const GetPlayerInfoByPlayerIdAPI = async (playerId) =>{
    try{
      const response = await Get_TeamPlayer_By_PlayerId_API(playerId)
      return response

    } catch(error){
      throw error
    }
  }
  ///////////////////////////////// End of API Calling ///////////////////////////////////////////////////////

  ////////////////////// End of Team List /////////////////////////////////////////////////////////////////


  ////////////////// Start Match List Module ////////////////////////////////////////////////////////////////

  ////////////////////////// Get Match Type for recent Match List ////////////////////////////////////////////////
  const GetMatchType = async ()=>{
    try{
      setNotes([])
      const response = await Get_Match_Type()
      setNotes(response)

    }
    catch(error){
      throw error
    }
  }

  /////////////////////////////Get Match list from the match type //////////////////////////////////////////////////
  const GetRecentMatchList = async (matchType)=>{
    try{
      setMatchList([])
      const response = await Get_Recent_Match(matchType)
      setMatchList(response)

    }
    catch(error){
      throw error
    }
  }

  /////////////////////////////////Get match Score of particular match id ///////////////////////////////////////

  
  const GetMatchScore = async (matchId)=>{
    try{
      setNotes([])
      const response = await Get_Recent_Match_Score(matchId)
      setNotes(response)

    }
    catch(error){
      throw error
    }
  }

  //////////////////////////////// Get Score of the batter and bowler from match id ///////////////////////////////////////////

  const GetMatchScoreBowler = async (matchId,teamId)=>{
    try{
      setNotes([])
      const response = await Get_Recent_Match_Score_Bowler(matchId,teamId)
      setNotes(response)

    }
    catch(error){
      throw error
    }
  }

  const GetMatchScoreBatter = async (matchId,teamId)=>{
    try{
      setNotes([])
      const response = await Get_Recent_Match_Score_Batter(matchId,teamId)
      setNotes(response)

    }
    catch(error){
      throw error
    }
  }

  /////////////////////////////////       END              ///////////////////////////////////////////////////////

  return (
    <NoteContext.Provider value={{ notes, GetTeamList, GetTeamPlayerList, GetPlayerDetailsList, teamName, GetTeamNameId ,GetPlayerNameId
                , GetTeamListAPI, GetPlayerByTeamIdAPI, GetPlayerInfoByPlayerIdAPI
                , GetMatchType , matchList ,GetRecentMatchList,GetMatchScore, GetMatchScoreBatter, GetMatchScoreBowler}}>
      {props.children}
    </NoteContext.Provider>
  );
};

export default NoteState;
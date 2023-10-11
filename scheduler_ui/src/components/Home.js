import React from 'react'
import { NavLink, Route, Routes } from 'react-router-dom'
// import Armor from "./Armor";
import Employee from './Employee';

function Home() {
  return (
    <>
    <div className="navContainer">
      <nav>
        <h1 id='EmployeeLink' >
            <NavLink to="employee">All Employee</NavLink>
        </h1>
      </nav>
    </div>
      <Routes>
        <Route path="employee" element={<Employee/>}/>
      </Routes>
    </>
  )
}

export default Home
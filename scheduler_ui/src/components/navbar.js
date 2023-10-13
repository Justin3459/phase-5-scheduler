import React, { useState } from "react";
import { NavLink, Route, Routes } from "react-router-dom";
import Home from './Home'
import Employee from './Employee'
import Availability from './Availability'
import Schedule from "./Schedule";
import Search from "./Search";
function Header({employee, handleDelete, setEmployee, dialogRef}){
    const [activeTab, setActiveTab] = useState("allStaff");
    
  //return console.log(employee)
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/allStaff" onClick={() => setActiveTab("allStaff")}>
            All Staff
          </NavLink>
        </li>
        <li>
          <NavLink to="/availability" onClick={() => setActiveTab("availability")}>
            Availability
          </NavLink>
        </li>
        <li>
          <NavLink to="/schedule" onClick={() => setActiveTab("schedule")}>
            Schedule
          </NavLink>
        </li>
        <li>
          <NavLink to="/search" onClick={() => setActiveTab("search")}>
            Search for Employee
          </NavLink>
        </li>
      </ul>

      <Routes>
        <Route path="*" element={<Home />}></Route>
        <Route
            path="allStaff"
            element={<Employee employee={employee} setEmployee = {setEmployee} handleDelete={handleDelete} />}
        ></Route>

        <Route
            path="availability"
            element= {<Availability/>}
        ></Route>

        <Route
            path="Schedule"
            element= {<Schedule/>}
        ></Route>

        <Route
            path="Search"
            element= {<Search/>}
        ></Route>
      </Routes>
    </nav>
  );
};

export default Header;
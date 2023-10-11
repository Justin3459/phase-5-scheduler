import React, { useState } from "react";
import { NavLink, Route, Routes } from "react-router-dom";

function NavBar(){
  const [activeTab, setActiveTab] = useState("allStaff");
  
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
    </nav>
  );
};

export default NavBar;
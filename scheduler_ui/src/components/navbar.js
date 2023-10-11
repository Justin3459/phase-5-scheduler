import React, { useState } from "react";
import { NavLink, Route, Routes } from "react-router-dom";
import Home from './Home'
import Employee from './Employee'
function NavBar(employee, setEmployee, dialogRef){
    const [activeTab, setActiveTab] = useState("allStaff");
    
    const handleDelete = (id) => {
        const filterEmployee = employee.filter((employee) => employee.id !== id);
    fetch(`http://localhost:3000/employee/${id}`, {
      method: "DELETE",
    })
      .then((r) => r.json())
      .then(setEmployee(filterEmployee));
  };

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
          path="employee"
          element={<Employee employee={employee} handleDelete={handleDelete} />}
        ></Route>
      </Routes>
    </nav>
  );
};

export default NavBar;
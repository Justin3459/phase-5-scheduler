import "./App.css";
import React, { useEffect, useRef, useState } from "react";
import Header from "./components/navbar";
import Card from "./components/Card";
import NavBar from "./components/navbar";
function App() {
  const [employee, setEmployee] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/employee")
      .then((r) => r.json())
      .then((data) => {
        setEmployee(data.map((employee) => employee));
      })
      .catch((error) => console.log("you shouldnt be here" + error));
  }, []);
  const handleDelete = (id)=> {
    const filterEmployeeByID = employee.filter((data) => data.id != id)
    fetch(`http://127.0.0.1:5000/employee/${id}`,{
      method: "DELETE",})
    .then((r) => r.json())
    .then(setEmployee(filterEmployeeByID))
    console.log(filterEmployeeByID)
  }

  const handlePatch = (id) => {
    const filterEmployeeByID = employee.filter((data) => data.id != id)
    fetch(`http://127.0.0.1:5000/employee/${id}`,{
      method: "PATCH",
    headers:{
      "Content-Type": "applicaiton/json",
    },
  body:JSON.stringify({
    
  })})
  }

  const dialogRef = useRef(null);
  const onEmployeeAdd = (empAdd) => setEmployee([...employee, empAdd]);

  //return console.log(employee)
  return (
    <div>
      <div className="header_container">
        <Header
          employee={employee}
          handleDelete={handleDelete}
          setEmployee={setEmployee}
          className="header"
        />
      </div>
      <div className="body_container">
        <ul></ul>
      </div>
    </div>
  );
}
export default App;

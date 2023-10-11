import './App.css';
import React, {useEffect, useRef, useState} from 'react'
import Header from "./components/navbar"

function App() {

  const [employee, setEmployee] = useState([])

  useEffect(()=>{
   fetch("http://127.0.0.1:5000/employee")
   .then(r =>r.json())
   .then(data => {
    setEmployee(data.map((employee)=>employee))})
   .catch(error => console.log("you shouldnt be here" + error))
  },[])

const dialogRef = useRef(null)
const onEmployeeAdd = empAdd => setEmployee([...employee, empAdd])

  return (
    <div>
      <div className='header_container'>
        <Header className="header"/>
      </div>
      <div className='body_container'>
        <ul>
          {employee.map((user) => (
            <li key={user.id}>{user.first_name}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};
export default App;

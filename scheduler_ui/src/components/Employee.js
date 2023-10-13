import React from "react";
import Card from "./Card";


function Employee({employee, setEmployee, handleDelete}) {
    const employeeMap = employee.map((data) => (
        <div key={data.id}>
          <h3>Name: {data.first_name} {data.last_name}</h3>
          <p>Email: {data.email}</p>
          <p>Phone Number: {data.phone_number}</p>
          {<button onClick={()=>{handleDelete(data.id)}} value={data.id}>Delete</button>}
          {/*<button onClick={handlePatch} value={data.id}>Edit</button>*/}
        </div>
      ))
    //return console.log(employee)
return (
    <div className="cardContainer">
        <h1>All Staff</h1>
        {employeeMap}
    </div>
  );
}

export default Employee;
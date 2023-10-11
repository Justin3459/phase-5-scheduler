import React from "react";
import Card from "./Card";


function Employee({employee, handleDelete}) {
return (
    <div className="cardContainer">
        <h1>All Staff</h1>
        <Card items={employee} handleDelete={handleDelete}/>
    </div>
  );
}

export default Employee;
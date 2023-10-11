import React from "react";
import Card from "./Card";


function Employee({employee, handleDelete}) {
return (
    <div className="cardContainer">
        <Card items={employee} handleDelete={handleDelete}/>
    </div>
  );
}

export default Employee;
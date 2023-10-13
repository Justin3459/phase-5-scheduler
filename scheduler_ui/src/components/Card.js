import React from "react";

function Card({employee,empmap, handleDelete}) {
  //const empArray = Object.values(employee)
  const empCheck = employee
  //const jsonParse = JSON.parse(employee)
    const employeeMap = employee.employee.map((data)=>(data))
  return console.log(employeeMap)
  /*return (
      <>
      {handleCard}
    </>
  );*/
}

export default Card;
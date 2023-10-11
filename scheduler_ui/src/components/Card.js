import React from "react";

function Card({employee = [], handleDelete}) {
  const itemArray = employee;
  const handleCard = itemArray.map((employee) => (
    <section key={employee.id} className="card">
      <h1 className="cardName">{employee.name}</h1>
      <img src={employee.image} alt={employee.first_name}></img>
      <p>Name: {employee.first_name} + {employee.last_name}</p>
      <p>email: {employee.email}</p>
      <p>Phone Number: {employee.phone_number}</p>
      <p>job: {employee.job}</p>
      <p>username: {employee.username}</p>
      <button onClick={()=>handleDelete(employee.id)} value={employee.id}>Delete</button>
    </section>
  ));

  return (
    <>
      {handleCard}
    </>
  );
}

export default Card;
import React from "react";
// import styles from "./CircleSelector.module.css";

import "./CircleSelector.css";

// NOTE: The <CircleSelector> component is responsible for letting <App> know that the user wants to select a certain circle in the <Circles> component.

// const CircleSelector = (props) => {
//   return <div className="CircleSelector">text button</div>

// {props.circles.map(color, idx => {
//   <button key={color} className="CircleSelector button"
//   style={{
//     backgroundColor: props.selColorIdx === idx ? 'white' : color,
//     borderColor: color
//   }}
//   onClick={() => props.handleColorSelection(idx)}
// />
// })}

//

// export default CircleSelector;

const CircleSelector = () => {
  // return <div> this is a div</div>;

  return (
    <div className="CircleSelector">
      <button className="CircleSelector">select circle 1</button>
      <button className="CircleSelector">select circle 2</button>
      <button className="CircleSelector">select circle 3</button>
      <button className="CircleSelector">select circle 4</button>
    </div>
  );
};

export default CircleSelector;

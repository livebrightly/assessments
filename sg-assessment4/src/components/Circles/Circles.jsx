import React, { useEffect, useState } from "react";
import CirclesCSS from "./Circles.css";

const Circles = () => {
  const [isActiveCircle, setActiveCircle] = useState(false);

  const handleClick = () => {
    console.log("handleClick function has run");
    setActiveCircle((currentCircle) => !currentCircle);
  };

  return (
    <div className="Circles">
      <div className="Circles" onClick={() => handleClick()}>
        1
      </div>
      <div className="Circles">2</div>
      <div className="Circles">3</div>
      <div className="Circles">4</div>
    </div>
  );
};

//* older code:
// <div
//  className={isActiveCircle ? "Circles" : ""}>

// className="Circles"
//   style={{
//     backgroundColor: isActiveCircle ? "transparent" : "",
//     color: isActiveCircle ? "purple" : "",
//     border: isActiveCircle ? "4px solid purple" : "",
//   }}
// onClick={() => setActiveCircle}
//   onClick={handleClick}
// >
//   1
// {
//  <div className={isActiveCircle ? "Circles" : ""}>
// <div        className="Circles"
//   style={{
//     backgroundColor: isActiveCircle ? "transparent" : "",
//     color: isActiveCircle ? "purple" : "",
//     border: isActiveCircle ? "4px solid purple" : "",
//   }}
// onClick={() => setActiveCircle}
// onClick={handleClick}
// >
// 1
//</div>
// <div
//   style={{
//     backgroundColor: isActiveCircle ? "transparent" : "",
//     color: isActiveCircle ? "purple" : "",
//     border: isActiveCircle ? "4px solid purple" : "",
//   }}
//   onClick={handleClick}
//   className="Circles"
// >
//   2
// </div>
// <div
//   style={{
//     backgroundColor: isActiveCircle ? "transparent" : "",
//     color: isActiveCircle ? "purple" : "",
//     border: isActiveCircle ? "4px solid purple" : "",
//   }}
//   onClick={handleClick}
//   className="Circles"
// >
//   3
// </div>
// <div
//   style={{
//     backgroundColor: isActiveCircle ? "transparent" : "",
//     color: isActiveCircle ? "purple" : "",
//     border: isActiveCircle ? "4px solid purple" : "",
//   }}
//   onClick={handleClick}
//   className="Circles"
// >
//   4
// </div>
//     }
//   );
// };

export default Circles;

// TODO: clean up the styles in the returned divs by getting the following to work

// move the toggle from styles in each div to clean up code

// const toggleStyle = () => {
//   const [isToggleStyle, setToggleStyle] = useState(false)
// };
// const toggleStyle = () => {
//   const [isToggleStyle, setToggleStyle] = useState(false, {
//     style : {
//       backgroundColor: isToggleStyle ? "transparent" : "",
//       color: isToggleStyle ? "purple" : "",
//       border: isToggleStyle ? "4px solid purple" : "",
//   }
// });

// const handleClick = () => {
//   console.log("handleClick function has run");
//   setActiveCircle((currentCircle) => !currentCircle);
// };

// const toggleStyle = () => {
//   const [isToggleStyle, setToggleStyle] = useState({
//     style : {
//       backgroundColor: isActiveCircle ? "transparent" : "",
//       color: isActiveCircle ? "purple" : "",
//       border: isActiveCircle ? "4px solid purple" : "",
//   }
// });

// (updating the DOM)
// useEffect(()=>{
//   console.log("toggleStyle function has run (useEffect)");
// }, []);

// modified to move the style components to a function
// const handleClick = (event) => {
//   console.log("handleClick function has run");
//   setToggleStyle({ ...isToggleStyle,
//     style:
//     {backgroundColor: event.target.value, color: event.target.value, border: event.target.value}})
// };

// const ToggleStyle = (props) => {
//   console.log("handleClick function has run");
//   const [isToggleStyle, setToggleStyle] = useState({
//     style: {
//       backgroundColor: isActiveCircle ? "transparent" : "",
//       color: isActiveCircle ? "purple" : "",
//       border: isActiveCircle ? "4px solid purple" : "",
//     },
//   });
// };
// TODO Ends

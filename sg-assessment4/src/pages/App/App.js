import React, { Component } from "react";
import "./App.css";
import Circles from "../../components/Circles/Circles";
import CircleSelector from "../../components/CircleSelector/CircleSelector";

class App extends Component {
  render() {
    const handleClick = () => {
      console.log("handleClick function has run");
    };

    return (
      <div className="App">
        <header className="App-header">UNIT 4 FINAL ASSESSMENT</header>
        <main>
          {/* purpose of the variable why am I passing the data */}

          {/* component CircleSelector */}
          <CircleSelector />

          {/* <div className="CircleSelector">
            <button className="button.selected">select circle 1</button>
            <button className="button">select circle 2</button>
            <button className="button">select circle 3</button>
            <button className="button">select circle 4</button>
          </div> */}

          {/* circle component */}

          <Circles />

          {/* <div className="Circles">
            <button onClick={handleClick} className="Circles">
              1
            </button>
            <button onClick={handleClick} className="Circles">
              2
            </button>
            <button onClick={handleClick} className="Circles">
              3
            </button>
            <button onClick={handleClick} className="Circles">
              4
            </button>
          </div> */}
        </main>
      </div>
    );
  }
}

// function App() {

//   return (
//     <div className="App">
//       <header className="App-header">UNIT 4 FINAL ASSESSMENT</header>
//       <main>

//       </main>
//     </div>
//   );
// }

export default App;

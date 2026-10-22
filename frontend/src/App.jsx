import { BrowserRouter, Routes, Route } from "react-router-dom";
import Homepage from "./pages/Homepage";
import EquipoForm from "./pages/EquipoForm";
import Navbar from "./components/Navbar";

function App() {
  return (
    <BrowserRouter>
      <div className="container mx-auto px-10">
        <Navbar />
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route path="/equipos/new" element={<EquipoForm />} />
          <Route path="/equipos/:id" element={<EquipoForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
import { useEffect, useState } from "react";
import { fetchEquipos } from "../api/equipos";
import EquipoList from "../components/EquipoList";

function Homepage() {
  const [equipos, setEquipos] = useState([]);

  useEffect(() => {
    fetchEquipos()
      .then((res) => setEquipos(res.data))
      .catch((err) => console.log(err));
  }, []);

  return <EquipoList equipos={equipos} />;
}

export default Homepage;
import EquipoCard from "./EquipoCard";

function EquipoList({ equipos }) {
  return (
    <div className="grid grid-cols-3 gap-4">
      {equipos.map((equipo) => (
        <EquipoCard equipo={equipo} key={equipo._id} />
      ))}
    </div>
  );
}

export default EquipoList;
import { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { fetchEquipo, createEquipo, updateEquipo, deleteEquipo } from "../api/equipos";

function EquipoForm() {
  const [equipo, setEquipo] = useState("");
  const [marcaSpecs, setMarcaSpecs] = useState("");
  const [precioVenta, setPrecioVenta] = useState(0);
  const params = useParams();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      if (!params.id) {
        await createEquipo({ 
          equipo, 
          marca_specs: marcaSpecs, 
          precio_venta: parseFloat(precioVenta) 
        });
      } else {
        await updateEquipo(params.id, { 
          equipo, 
          marca_specs: marcaSpecs, 
          precio_venta: parseFloat(precioVenta) 
        });
      }
      navigate("/");
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    if (params.id) {
      fetchEquipo(params.id)
        .then((res) => {
          setEquipo(res.data.equipo);
          setMarcaSpecs(res.data.marca_specs || "");
          setPrecioVenta(res.data.precio_venta || 0);
        })
        .catch((err) => console.log(err));
    }
  }, [params.id]);

  return (
    <div className="flex items-center justify-center h-[calc(100vh-10rem)]">
      <div>
        <form className="bg-zinc-950 p-10 rounded" onSubmit={handleSubmit}>
          <h1 className="text-3xl font-bold my-4">
            {params.id ? "Actualizar Equipo" : "Crear Equipo"}
          </h1>
          
          <input
            type="text"
            placeholder="Equipo"
            className="block py-2 px-3 mb-4 w-full text-black rounded"
            onChange={(e) => setEquipo(e.target.value)}
            value={equipo}
            autoFocus
          />
          
          <textarea
            placeholder="Marca y Especificaciones"
            className="block py-2 px-3 mb-4 w-full text-black rounded"
            rows="3"
            onChange={(e) => setMarcaSpecs(e.target.value)}
            value={marcaSpecs}
          ></textarea>

          <input
            type="number"
            placeholder="Precio de Venta"
            className="block py-2 px-3 mb-4 w-full text-black rounded"
            onChange={(e) => setPrecioVenta(e.target.value)}
            value={precioVenta}
          />

          <button className="bg-white hover:bg-slate-800 hover:text-white text-slate-800 py-2 px-4 rounded w-full font-bold">
            {params.id ? "Actualizar Equipo" : "Guardar Equipo"}
          </button>
        </form>

        {params.id && (
          <button
            className="bg-red-500 hover:bg-red-400 text-white font-bold py-2 px-4 rounded mt-5 w-full"
            onClick={async () => {
              try {
                await deleteEquipo(params.id);
                navigate("/");
              } catch (error) {
                console.log(error);
              }
            }}
          >
            Borrar Equipo
          </button>
        )}
      </div>
    </div>
  );
}

export default EquipoForm;
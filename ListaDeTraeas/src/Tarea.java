public class Tarea {
    private boolean completada;
    private String descripcion;
    private String fecha;
    
    public Tarea(String descripcion, String fecha, boolean completada){
        this.descripcion = descripcion;
        this.fecha = fecha;
        this.completada = completada;

    }
    public String getDescripcion() {
        return descripcion;
    }
    public void setDescripcion(String descripcion){
        this.descripcion=descripcion;
    }
    public String getFecha(){
        return fecha;
    }
    public void setFecha(String fecha){
        this.fecha=fecha;
    }
    public boolean isCompletada(){
        return completada;
    }
    public void setCompletada(boolean completada){
        this.completada=completada;
    }

    @Override //Para que el metodo toString() sea llamado por el metodo println()
    public String toString(){
        return (completada? "✔ " : "✘ ") + descripcion + " (" + fecha + ")";
    }


}



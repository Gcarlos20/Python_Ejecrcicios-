// nombre del codigo SHIVA
import java.util.ArrayList;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import java.awt.BorderLayout;

public class Main {
    private JFrame frame; //Para acceder a la ventana principal
    private DefaultListModel<Tarea> listaTareas; //Para acceder a la lista de tareas
    private JList<Tarea> jListTareas; // 
    private ArrayList<Tarea> tareas;

   
    public Main(){
        tareas = new ArrayList<>();
        iniciarInterfaz(); //Llamada al método que inicia la interfaz
    }
    private void iniciarInterfaz(){
        frame = new JFrame("Lista De Tareas"); //Crea la ventana principal
        frame.setSize(500, 500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Cierra la ventana cuando se pulsa la tecla X
        frame.setLayout(new BorderLayout()); // Para que el layout sea vertical

        listaTareas = new DefaultListModel<>();
        jListTareas = new JList<>(listaTareas);

        JScrollPane scroll = new JScrollPane(jListTareas);

        //Crea el panel de botones
        JButton btnAgregar = new JButton("Agregar");
        JButton btnEliminar = new JButton("Eliminar");
        JButton btnCompletar = new JButton("Completar");
        JButton btnCancelar = new JButton("Cancelar");
        JButton btnSalir = new JButton("Salir");

        //Agrega el panel de botones a la ventana principal
            JPanel panelBotones = new JPanel();
        panelBotones.add(btnAgregar);
        panelBotones.add(btnEliminar);
        panelBotones.add(btnCompletar);
        panelBotones.add(btnCancelar);
        panelBotones.add(btnSalir);


        frame.add(scroll, BorderLayout.CENTER);
        frame.add(panelBotones, BorderLayout.SOUTH);


        btnAgregar.addActionListener(e -> agregarTarea());
        btnEliminar.addActionListener(e -> eliminarTarea());
        btnCompletar.addActionListener(e -> completarTarea());
        btnCancelar.addActionListener(e -> cancelar());

        frame.setVisible(true);
    }

    private void agregarTarea(){
        String descripcion = JOptionPane.showInputDialog("Ingrese la descripcion de la tarea");
         String fecha = JOptionPane.showInputDialog(frame, "Fecha:");
         if (descripcion != null && fecha != null){
            Tarea tarea = new Tarea(descripcion, fecha, false);
            tareas.add(tarea);
            listaTareas.addElement(tarea);
         }

    }

    private void eliminarTarea() {
        int index = jListTareas.getSelectedIndex();
        if (index >= 0) {
            tareas.remove(index);
            listaTareas.remove(index);
        }
    }

    private void completarTarea() {
        int index = jListTareas.getSelectedIndex();
        if (index >= 0) {
            tareas.get(index).setCompletada(true);
            listaTareas.set(index, tareas.get(index));
        }
    }
    private void cancelar(){
        frame.dispose();
    }

    public static void main(String[] args) {
        new Main();
    }

}

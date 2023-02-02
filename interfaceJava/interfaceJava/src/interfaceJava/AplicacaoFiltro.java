package interfaceJava;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.GridLayout;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

public class AplicacaoFiltro extends JFrame {

	private JPanel Frame;
	public String camImagem;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					AplicacaoFiltro frame = new AplicacaoFiltro();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public void ExecutarScriptPython(String saida) {
        try {
        	cmdExec[3] = saida; 
		    Runtime.getRuntime().exec(cmdExec);
		    
		    Thread.sleep(2200);
		    
		    SubstituirTexto(saida);
		    SubstituirImagem(saida);


        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	
	public void addCentro(JPanel centro) {
		JPanel Esq = new JPanel();centro.add(Esq, BorderLayout.WEST);Esq.setPreferredSize(new Dimension(100, 100));
		JPanel cima = new JPanel();centro.add(cima, BorderLayout.NORTH);cima.setPreferredSize(new Dimension(100, 100));
		JPanel dir = new JPanel();centro.add(dir, BorderLayout.EAST);dir.setPreferredSize(new Dimension(100, 100));
		JPanel baixo = new JPanel();centro.add(baixo, BorderLayout.SOUTH);baixo.setPreferredSize(new Dimension(100, 100));
		
		JPanel meio = new JPanel();
		centro.add(meio, BorderLayout.CENTER);
		meio.setLayout(new GridLayout(1, 0, 0, 0));
		
		JLabel imgOriginal = new JLabel("Img Original");
		meio.add(imgOriginal);
		
		JLabel imgEditada = new JLabel("Img Editada");
		meio.add(imgEditada);
		
		ExecutarScriptPython(this.camImagem);
		
		ImageIcon imagem = new ImageIcon(this.camImagem);
		imagem.setImage(imagem.getImage().getScaledInstance(200, 200, java.awt.Image.SCALE_SMOOTH));
		imgOriginal.setIcon(imagem);
	}
	
	public void inicializeFrame() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(400, 400);
		
		Frame = new JPanel();
		setContentPane(Frame);
		Frame.setLayout(new BorderLayout(0, 0));
		
		JPanel centro = new JPanel();
		Frame.add(centro, BorderLayout.CENTER);
		centro.setLayout(new BorderLayout(0, 0));
		
		addCentro(centro);
	}
	
	/**
	 * Create the frame.
	 */
	public AplicacaoFiltro() {			
		
		inicializeFrame();	
	}
	
	public AplicacaoFiltro(String cam) {			
		
		this.camImagem = cam;
		inicializeFrame();
	}
}

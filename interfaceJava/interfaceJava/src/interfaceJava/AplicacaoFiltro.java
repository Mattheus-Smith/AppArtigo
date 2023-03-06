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
	FuncoeExtras funcExtras;
	String definirDiretorio;

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
	
	public void addCentro(JPanel centro) {
		JPanel Esq = new JPanel();centro.add(Esq, BorderLayout.WEST);Esq.setPreferredSize(new Dimension(50, 50));
		JPanel cima = new JPanel();centro.add(cima, BorderLayout.NORTH);cima.setPreferredSize(new Dimension(50, 50));
		JPanel dir = new JPanel();centro.add(dir, BorderLayout.EAST);dir.setPreferredSize(new Dimension(50, 50));
		JPanel baixo = new JPanel();centro.add(baixo, BorderLayout.SOUTH);baixo.setPreferredSize(new Dimension(50, 50));
		
		JPanel meio = new JPanel();
		centro.add(meio, BorderLayout.CENTER);
		meio.setLayout(null);
		
		JLabel imgOriginal = new JLabel();
		imgOriginal.setLocation(0, 0);
		imgOriginal.setSize(new Dimension(392, 561));
		meio.add(imgOriginal);
		
		JLabel imgEditada = new JLabel();
		imgEditada.setBounds(392, 0, 392, 561);
		imgEditada.setPreferredSize(new Dimension(50, 50));
		meio.add(imgEditada);
		
		ImageIcon imagem = new ImageIcon(funcExtras.camImagem);
		imagem.setImage(imagem.getImage().getScaledInstance(imgOriginal.getWidth(), imgOriginal.getHeight(), java.awt.Image.SCALE_SMOOTH));
		imgOriginal.setIcon(imagem);
		
		ImageIcon imagemEditada = new ImageIcon(funcExtras.camImagemEditada);
		imagemEditada.setImage(imagemEditada.getImage().getScaledInstance(imgEditada.getWidth(), imgEditada.getHeight(), java.awt.Image.SCALE_SMOOTH));
		imgEditada.setIcon(imagemEditada);
	}
	
	
	public void inicializeFrame() {
		
		this.definirDiretorio = "1";
		funcExtras.definirDiretorios(this.definirDiretorio);
		
		setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
		setSize(900, 700);
		
		Frame = new JPanel();
		setContentPane(Frame);
		Frame.setLayout(new BorderLayout(0, 0));
		
		funcExtras.ExeScriptPythonFiltro(funcExtras.camImagem, definirDiretorio, funcExtras.tipoProblema);
		
		
		
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
	
	public AplicacaoFiltro(FuncoeExtras funcE) {			
		this.funcExtras = funcE;
		inicializeFrame();
	}
}
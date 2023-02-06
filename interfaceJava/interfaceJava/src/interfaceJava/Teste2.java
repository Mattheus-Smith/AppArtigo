package interfaceJava;

import java.awt.EventQueue;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;

public class Teste2 extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Teste2 frame = new Teste2();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Teste2() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 888, 578);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel();
		lblNewLabel.setBounds(56, 29, 315, 462);
		ImageIcon imagem = new ImageIcon("");
		imagem.setImage(imagem.getImage().getScaledInstance(lblNewLabel.getWidth(), lblNewLabel.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblNewLabel.setIcon(imagem);
		contentPane.add(lblNewLabel);
		
		JLabel lblFiltrada = new JLabel();
		lblFiltrada.setBounds(481, 29, 315, 462);
		ImageIcon imagem2 = new ImageIcon("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens\\19.jpg");
		imagem2.setImage(imagem2.getImage().getScaledInstance(lblFiltrada.getWidth(), lblFiltrada.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblNewLabel.setIcon(imagem2);
		contentPane.add(lblFiltrada);
	}
	
	public Teste2(FuncoeExtras funcExtras) {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 1194, 578);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel();
		lblNewLabel.setBounds(56, 29, 315, 462);
		ImageIcon imagem = new ImageIcon(funcExtras.camImagem);
		imagem.setImage(imagem.getImage().getScaledInstance(lblNewLabel.getWidth(), lblNewLabel.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblNewLabel.setIcon(imagem);
		contentPane.add(lblNewLabel);
		
		JLabel lblFiltrada = new JLabel();
		lblFiltrada.setBounds(481, 29, 315, 462);
		ImageIcon imagem2 = new ImageIcon("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens\\19.jpg");
		imagem2.setImage(imagem2.getImage().getScaledInstance(lblFiltrada.getWidth(), lblFiltrada.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblNewLabel.setIcon(imagem2);
		contentPane.add(lblFiltrada);
	}
	
	
}

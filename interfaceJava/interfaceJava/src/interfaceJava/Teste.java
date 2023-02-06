package interfaceJava;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.EventQueue;
import java.awt.GridLayout;

import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;

public class Teste extends JFrame {

	private JPanel Frame;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Teste frame = new Teste();
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
	public Teste() {
		
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(900, 700);
		
		Frame = new JPanel();
		//Frame.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(Frame);
		Frame.setLayout(new BorderLayout(0, 0));
		
		JPanel panel = new JPanel();
		Frame.add(panel, BorderLayout.NORTH);
		
		JPanel panel_1 = new JPanel();
		Frame.add(panel_1, BorderLayout.WEST);
		
		JPanel panel_2 = new JPanel();
		Frame.add(panel_2, BorderLayout.EAST);
		
		JPanel panel_3 = new JPanel();
		Frame.add(panel_3, BorderLayout.SOUTH);
		
		JPanel meio = new JPanel();
		Frame.add(meio, BorderLayout.CENTER);
		meio.setLayout(new GridLayout(0, 2, 0, 0));
		
		JLabel lblNewLabel_1 = new JLabel("New label");
		meio.add(lblNewLabel_1);
		
		ImageIcon imagem = new ImageIcon("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\imgFiltrada.png");
		imagem.setImage(imagem.getImage().getScaledInstance(lblNewLabel_1.getWidth(), lblNewLabel_1.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblNewLabel_1.setIcon(imagem);
		
		JLabel lblNewLabe_2 = new JLabel("New label");
		meio.add(lblNewLabe_2);
		
		ImageIcon imagem2 = new ImageIcon("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\imgFiltrada.png");
		imagem2.setImage(imagem2.getImage().getScaledInstance(lblNewLabe_2.getWidth(), lblNewLabe_2.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblNewLabe_2.setIcon(imagem2);
		
	}

}

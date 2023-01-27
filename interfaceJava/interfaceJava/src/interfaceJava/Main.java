package interfaceJava;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileSystemView;

import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JButton;
import java.awt.GridLayout;
import javax.swing.JTextPane;
import javax.swing.SwingConstants;

import java.awt.Button;
import java.awt.Label;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.awt.Component;
import java.awt.ComponentOrientation;

import javax.swing.Box;
import java.awt.Font;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.TextField;

public class Main extends JFrame {

	private JPanel contentPane;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Main frame = new Main();
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
	public Main() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(600, 600);
		
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		Button btnEsq = new Button("Ler imagem");
		btnEsq.setBounds(50, 50, 170, 90);
		//add funcão de clicavel para adicionar a leitura da imagem
		
		JButton btnCarregarFoto = new JButton("...");
		btnCarregarFoto.setForeground(UIManager.getColor("Button.light"));
		btnCarregarFoto.setBackground(new Color(0, 38, 51));
		btnCarregarFoto.setPreferredSize(new Dimension(20, 100));
		
		btnEsq.addActionListener((ActionListener) new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				JFileChooser jfc = new JFileChooser(FileSystemView.getFileSystemView());
				jfc.setDialogTitle("Choose a directory to save your file: teste ");
				jfc.setAcceptAllFileFilterUsed(false);
				FileNameExtensionFilter filter = new FileNameExtensionFilter("PNG and JPEG images", "png", "jpeg");
				jfc.setFileFilter(filter);

				int returnValue = jfc.showSaveDialog(null);
				if (returnValue == JFileChooser.APPROVE_OPTION) {
					if (jfc.getSelectedFile().isDirectory()) {
						System.out.println("You selected the directory: " + jfc.getSelectedFile());
					}
				}
				JOptionPane.showMessageDialog(null, "Arquivo selecionado");
				String saida = jfc.getSelectedFile().getPath() ;				
				//fotoInfo1.replaceSelection(saida);
			}
		});
		
//		btnEsq.addActionListener((ActionListener) new ActionListener() {
//			public void actionPerformed(ActionEvent e) {
//				try {					
//					
//					File file = new File("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\cidadeEscura.jpg");
//			        BufferedImage bufferedImage = ImageIO.read(file);
//
//			        ImageIcon imageIcon = new ImageIcon(bufferedImage);
//			        JFrame jFrame = new JFrame();
//
//			        jFrame.setSize(500, 500);
//			        JLabel jLabel = new JLabel();
//
//			        jLabel.setIcon(imageIcon);
//			        jFrame.getContentPane().add(jLabel);
//			        jFrame.setVisible(true);
//
//			        jFrame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE );
//				
//					
//				} catch (IOException e1) {
//					// TODO Auto-generated catch block
//					e1.printStackTrace();
//				}
//			}
//		});
		
//		JLabel iconConfirmar = new JLabel(new ImageIcon("./imagens/Seach_white.png"));
//		BotaoPesquisar.add(iconConfirmar);
//		
//		BotaoPesquisar.addMouseListener(new java.awt.event.MouseAdapter() {
//		    public void mouseEntered(java.awt.event.MouseEvent evt) {
//		    	BotaoPesquisar.setBackground(new Color(255, 255, 255));
//		    	Botao.setForeground(new Color(0, 0, 51));	
//		    	iconConfirmar.setIcon(new ImageIcon("./imagens/Seach_Black.png"));
//		    }
//		    public void mouseExited(java.awt.event.MouseEvent evt) {
//		    	BackgroundBarraNav(BotaoPesquisar);
//		    	Botao.setForeground(new Color(255, 255, 255));
//		    	iconConfirmar.setIcon(new ImageIcon("./imagens/Seach_white.png"));
//		    }
//		});
		
		contentPane.add(btnEsq);
		
		Label label_OU = new Label("OU");
		label_OU.setFont(new Font("Yu Gothic", Font.BOLD, 15));
		label_OU.setAlignment(Label.CENTER);
		label_OU.setBounds(234, 50, 130, 90);
		contentPane.add(label_OU);
		
		Button btnDrt = new Button("Escolher imagem aleatória");
		btnDrt.setBounds(380, 50, 170, 90);
		contentPane.add(btnDrt);
	}
}

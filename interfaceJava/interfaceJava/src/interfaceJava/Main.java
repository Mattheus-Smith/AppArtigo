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
import java.io.*;

public class Main extends JFrame {

	static final Runtime run = Runtime.getRuntime();
    static Process pro;
    static BufferedReader read;
	private JPanel Frame;

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
	
	private static void showFB() throws IOException
    {
        read = new BufferedReader(new InputStreamReader(pro.getInputStream()));
        System.out.println(read.readLine());
    }
    
	
	public void ExecutarScriptPython(String saida) {
		String texto1 = "python C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py";
		
		String texto = "C:\\\\Users\\\\Public\\\\teste\\\\main.py";
		String Start = "cmd /c start cmd.exe";

        try {
        	//Runtime.getRuntime().exec("python C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py");

        	//since exec has its own process we can use that
//        	ProcessBuilder builder = new ProcessBuilder("python", "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py");
//        	builder.directory(new File("C:\\"));
//        	builder.redirectError();
//
//        	Process newProcess = builder.start();
        	
//        	String command = "cmd.exe /c start python C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py";
//        	Process p = Runtime.getRuntime().exec(command);
        	
        	ProcessBuilder builder = new ProcessBuilder("python", texto);
        	builder.directory(new File("python"));
        	builder.redirectError();
        	Process newProcess = builder.start();
//            pro = run.exec(command);
//            showFB();//Mostra as resposta
        	
//        	ProcessBuilder builder = new ProcessBuilder();
//        	builder.command("cmd.exe", "/c", "python" ,texto);
//        	pro = builder.start();
        	//pro = run.exec(texto);
            //showFB();//Mostra as resposta

        } catch(Exception e) {
            System.err.println(e);
        }
	}

	/**
	 * Create the frame.
	 */
	public Main() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(600, 600);
		
		Frame = new JPanel();
		Frame.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(Frame);
		Frame.setLayout(null);
		
		String output = "aq";
		Button btnEsq = new Button("Ler imagem");
		
		
		btnEsq.setBounds(50, 50, 170, 90);
		//funcão de click para fazer a leitura da imagem
		btnEsq.addActionListener((ActionListener) new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				//JFileChooser jfc = new JFileChooser(FileSystemView.getFileSystemView());
				
				JFileChooser jfc = new JFileChooser("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\imagens");	//pc Projeto
				jfc.setDialogTitle("Choose a directory to save your file: teste ");
				jfc.setAcceptAllFileFilterUsed(false);
				FileNameExtensionFilter filter = new FileNameExtensionFilter("PNG, JPEG and JPG images", "png", "jpeg", "jpg");
				jfc.setFileFilter(filter);

				int returnValue = jfc.showSaveDialog(null);
				//JOptionPane.showMessageDialog(null, "Arquivo selecionado");
				String saida = jfc.getSelectedFile().getPath() ;
				//fotoInfo1.replaceSelection(saida);
				System.out.print("voce selecionou essa imagem: "+ saida+"\n");
				
				//executar codigo em python
				ExecutarScriptPython(saida);
			}
		});
		
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
		
		Frame.add(btnEsq);
		
		Label label_OU = new Label("OU");
		label_OU.setFont(new Font("Yu Gothic", Font.BOLD, 15));
		label_OU.setAlignment(Label.CENTER);
		label_OU.setBounds(234, 50, 130, 90);
		Frame.add(label_OU);
		
		Button btnDrt = new Button("Escolher imagem aleatória");
		btnDrt.setBounds(380, 50, 170, 90);
		Frame.add(btnDrt);
	}
}

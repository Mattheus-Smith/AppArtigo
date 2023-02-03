package interfaceJava;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.util.Random;

import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileSystemView;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;

import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.Insets;
import java.awt.Button;
import java.awt.Label;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.util.List;
import java.awt.Component;
import java.awt.ComponentOrientation;
import java.awt.Font;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.TextField;
import java.io.*;
import java.nio.file.Files;

public class Main extends JFrame {

	static final Runtime run = Runtime.getRuntime();
    static Process pro;
    static BufferedReader read;
	private JPanel Frame;
	JPanel panel;
	JPanel topo;
	JPanel centro;
	JPanel footer;
	JPanel infoDireita;
	JPanel meio;
	Button btnDrt;
	Label nomeImagem;
	Label textOutput;
	JLabel lblimagem;
	JLabel lblhistograma;
	ImageIcon histo;
	ImageIcon imagem;
	
	String definirDiretorio;
	FuncoeExtras funcExtras;
	
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
	
	public void funcRetirarIdDoTexto(String texto, String[] textoFiltrado) {
		String id = texto.substring(0,1);
		String saida =  texto.substring(2,texto.length());
		
		textoFiltrado[0] = id;
		textoFiltrado[1] = saida;
	}
	
	public void SubstituirTexto(String img) throws IOException {
		
		String nome = img.substring(img.length() - 6, img.length());
		nomeImagem.setText(nome);
	    
	    BufferedReader texto = new BufferedReader(new InputStreamReader(new FileInputStream(funcExtras.arq), "UTF-8"));
	    String linha = new String(texto.readLine().getBytes(), "UTF-8");
	    
	    String[] textoFiltrado = {"",""};
	    funcRetirarIdDoTexto(linha, textoFiltrado);
	    
	    funcExtras.tipoProblema = textoFiltrado[0];
	    textOutput.setText(textoFiltrado[1]);
	    texto.close();
	}
	
	public void SubstituirImagem(String img) throws IOException {
		
		imagem = new ImageIcon(img);
		imagem.setImage(imagem.getImage().getScaledInstance(lblimagem.getWidth(), lblimagem.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblimagem.setIcon(imagem);
		
		histo = new ImageIcon(funcExtras.camHistoOriginal);
		histo.setImage(histo.getImage().getScaledInstance(lblhistograma.getWidth(), lblhistograma.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblhistograma.setIcon(histo);

	}

	public void addMeioTopo(JPanel meio) {

		Button btnEsq = new Button("Ler imagem");
		//funcão de click para fazer a leitura da imagem
		btnEsq.addActionListener((ActionListener) new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				//JFileChooser jfc = new JFileChooser(FileSystemView.getFileSystemView());
				
				funcExtras.jfc.setDialogTitle("Choose a directory to save your file: teste ");
				funcExtras.jfc.setAcceptAllFileFilterUsed(false);
				FileNameExtensionFilter filter = new FileNameExtensionFilter("PNG, JPEG and JPG images", "png", "jpeg", "jpg");
				funcExtras.jfc.setFileFilter(filter);

				int returnValue = funcExtras.jfc.showSaveDialog(null);
				//JOptionPane.showMessageDialog(null, "Arquivo selecionado");
				String saida = funcExtras.jfc.getSelectedFile().getPath() ;
				//System.out.print("voce selecionou essa imagem: "+ saida+"\n");
				funcExtras.camImagem = saida;
				//executar codigo em python
				funcExtras.ExecutarScriptPython(saida, definirDiretorio);
				
				try {
					SubstituirTexto(saida);
					SubstituirImagem(saida);
				} catch (IOException e1) {
					// TODO Auto-generated catch block
					e1.printStackTrace();
				}
				
				//funcão de click para fazer a leitura da imagem se estiver uma imagem armazenada
				btnDrt.addActionListener((ActionListener) new ActionListener() {
					public void actionPerformed(ActionEvent e) {
						
						AplicacaoFiltro af = new AplicacaoFiltro(funcExtras);
						af.setVisible(true);
					}
				});
			}
		});
	
		meio.add(btnEsq);
		
		Label label_OU = new Label();
		label_OU.setAlignment(Label.CENTER);
		label_OU.setFont(new Font("Yu Gothic", Font.BOLD, 15));
		label_OU.setBounds(381, 50, 130, 90);
		meio.add(label_OU);
		
		btnDrt = new Button("Aplicar filtro");
		meio.add(btnDrt);
	}
	

	public void addTopo(JPanel topo) {
		
		JPanel drt = new JPanel();
		drt.setPreferredSize(new Dimension(100, 25));
		topo.add(drt, BorderLayout.WEST);
		
		JPanel esq = new JPanel();
		esq.setPreferredSize(new Dimension(100, 25));
		topo.add(esq, BorderLayout.EAST);

		JPanel cima = new JPanel();
		cima.setPreferredSize(new Dimension(100, 20));
		topo.add(cima, BorderLayout.NORTH);

		JPanel baixo = new JPanel();
		baixo.setPreferredSize(new Dimension(100, 20));
		topo.add(baixo, BorderLayout.SOUTH);
		
		meio = new JPanel();
		meio.setLayout(new BoxLayout(meio, BoxLayout.X_AXIS));
		topo.add(meio);
		addMeioTopo(meio);
		
	}
	
	public void addInformacoes(JPanel infoDireita) {
		
		nomeImagem = new Label();
		nomeImagem.setAlignment(Label.CENTER);
		nomeImagem.setPreferredSize(new Dimension(100, 80));
		nomeImagem.setFont(new Font("Yu Gothic", Font.BOLD, 24));
		infoDireita.add(nomeImagem, BorderLayout.NORTH);
		
		lblhistograma = new JLabel();
		infoDireita.add(lblhistograma, BorderLayout.CENTER);
		
		textOutput = new Label();
		textOutput.setAlignment(Label.CENTER);
		textOutput.setPreferredSize(new Dimension(100, 80));
		textOutput.setFont(new Font("Yu Gothic", Font.BOLD, 24));
		infoDireita.add(textOutput, BorderLayout.SOUTH);
		
	}
	
	public void addCentro(JPanel centro) {
		lblimagem = new JLabel();
		centro.add(lblimagem);
		
		infoDireita = new JPanel();
		infoDireita.setLayout(new BorderLayout(0, 0));
		centro.add(infoDireita);
		
		addInformacoes(infoDireita);
		
	}
	
	/**
	 * Create the frame.
	 */
	public Main() {
		
		this.definirDiretorio = "1";
		
		funcExtras = new FuncoeExtras(); 
		funcExtras.definirDiretorios(this.definirDiretorio);
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setSize(900, 700);
		
		Frame = new JPanel();
		//Frame.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(Frame);
		Frame.setLayout(new BorderLayout(0, 0));
		
		topo = new JPanel();
		topo.setLayout(new BorderLayout(0, 0));
		topo.setPreferredSize(new Dimension(100, 100));
		addTopo(topo);
		Frame.add(topo, BorderLayout.NORTH);
		
		centro = new JPanel();
		centro.setLayout(new GridLayout(0, 2, 0, 0));
		centro.setPreferredSize(new Dimension(100, 100));
		addCentro(centro);
		Frame.add(centro, BorderLayout.CENTER);
	}
}

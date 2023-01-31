package interfaceJava;

import java.awt.BorderLayout;
import java.awt.EventQueue;
import java.util.Random;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileSystemView;
import javax.swing.text.SimpleAttributeSet;
import javax.swing.text.StyleConstants;

import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JButton;
import java.awt.GridLayout;
import java.awt.Insets;

import javax.swing.JTextPane;
import javax.swing.SwingConstants;

import java.awt.Button;
import java.awt.Label;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.util.List;
import java.awt.Component;
import java.awt.ComponentOrientation;

import javax.swing.Box;
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
	JLabel lblimagem;
	JLabel lblhistograma;
	JPanel panel;
	JPanel topo;
	JPanel centro;
	JPanel footer;
	JPanel infoDireita;
	Label nomeImagem;
	Label textOutput;
	private JPanel meio_1;
	
	
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
	
	
	public void SubstituirTexto(String img) throws IOException {
		
		String nome = img.substring(img.length() - 6, img.length());
		nomeImagem.setText(nome);
		
		//String arqProjeto = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt";
		String arqPessoal = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.txt";
	    
	    BufferedReader texto = new BufferedReader(new InputStreamReader(new FileInputStream(arqPessoal), "UTF-8"));
	    String linha = new String(texto.readLine().getBytes(), "UTF-8");
	    textOutput.setText(linha);
	    texto.close();
	}
	
	public void SubstituirImagem(String img) throws IOException {
		
		ImageIcon imagem = new ImageIcon(img);
		imagem.setImage(imagem.getImage().getScaledInstance(lblimagem.getWidth(), lblimagem.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblimagem.setIcon(imagem);
		
		//ImageIcon histo = new ImageIcon("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.png");
		ImageIcon histo = new ImageIcon("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.png");
		histo.setImage(histo.getImage().getScaledInstance(lblhistograma.getWidth(), lblhistograma.getHeight(), java.awt.Image.SCALE_SMOOTH));
		lblhistograma.setIcon(histo);

	}

	public void ExecutarScriptPython(String saida) {
        try {

        	String[] cmdProjeto = {
        		      "python",
        		      "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py",
        		      "--img",
        		      saida
        		    };
        	String[] cmdPessoal = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\main.py",
	      		      "--img",
	      		      saida
      		    };
		    Runtime.getRuntime().exec(cmdPessoal);
		    
		    Thread.sleep(2000);
		    
		    SubstituirTexto(saida);
		    SubstituirImagem(saida);


        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	public void addMeioTopo(JPanel meio) {
		Button btnEsq = new Button("Ler imagem");
		//funcão de click para fazer a leitura da imagem
		btnEsq.addActionListener((ActionListener) new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				//JFileChooser jfc = new JFileChooser(FileSystemView.getFileSystemView());
				
				//JFileChooser jfc = new JFileChooser("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\imagens");	//pc Projeto
				JFileChooser jfc = new JFileChooser("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens");	//pc pessoal
				jfc.setDialogTitle("Choose a directory to save your file: teste ");
				jfc.setAcceptAllFileFilterUsed(false);
				FileNameExtensionFilter filter = new FileNameExtensionFilter("PNG, JPEG and JPG images", "png", "jpeg", "jpg");
				jfc.setFileFilter(filter);

				int returnValue = jfc.showSaveDialog(null);
				//JOptionPane.showMessageDialog(null, "Arquivo selecionado");
				String saida = jfc.getSelectedFile().getPath() ;
				System.out.print("voce selecionou essa imagem: "+ saida+"\n");
				
				//executar codigo em python
				ExecutarScriptPython(saida);
			}
		});
		meio_1.setLayout(new BoxLayout(meio_1, BoxLayout.X_AXIS));
		meio.add(btnEsq);
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
		
		Label label_OU = new Label("OU");
		label_OU.setAlignment(Label.CENTER);
		label_OU.setFont(new Font("Yu Gothic", Font.BOLD, 15));
		label_OU.setBounds(381, 50, 130, 90);
		meio.add(label_OU);
		
		Button btnDrt = new Button("Escolher imagem aleatória");
		//funcão de click para fazer a leitura da imagem
		btnDrt.addActionListener((ActionListener) new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				
				File file = new File("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\imagens");	//pc Projeto
				File[] arquivos = file.listFiles();
				
				Random random = new Random();
				int numero = random.nextInt(arquivos.length);
				String saida = arquivos[numero].toString();
				System.out.print("voce selecionou essa imagem: "+saida +"\n");
				
				//executar codigo em python
				ExecutarScriptPython(saida);
			}
		});
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
		
		meio_1 = new JPanel();
		topo.add(meio_1);
		addMeioTopo(meio_1);
		
		
		
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

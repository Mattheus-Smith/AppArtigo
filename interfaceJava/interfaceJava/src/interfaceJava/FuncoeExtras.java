package interfaceJava;

import java.awt.Button;
import java.awt.Label;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;

import javax.swing.ImageIcon;
import javax.swing.JFileChooser;
import javax.swing.JLabel;

public class FuncoeExtras {
	
	Label nomeImagem;
	Label textOutput;
	
	ImageIcon histo;
	ImageIcon imagem;
	String[] cmdExecEntrada;
	String[] cmdExecFiltro;
	JFileChooser jfc;
	
	String arq;
	String tipoProblema;
	String flagOutput;
	public String camHistoOriginal;
	public String camImagem;
	public String camImagemEditada;
	
	public void verificarSaida() throws UnsupportedEncodingException, IOException {
		BufferedReader texto = new BufferedReader(new InputStreamReader(new FileInputStream(flagOutput), "UTF-8"));
	    String linha = new String(texto.readLine().getBytes(), "UTF-8");
	    
	    while( linha != "1" ) {
	    	if(  linha == "1" ) {
	    		break;
	    	}
	    	texto = new BufferedReader(new InputStreamReader(new FileInputStream(flagOutput), "UTF-8"));
		    linha = new String(texto.readLine().getBytes(), "UTF-8");
	    	
	    }
	}
	
	public void definirDiretorios(String i) {
		//flagOutput = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\flagOutput.txt";		
		if( i == "0" ) {//pessoal
			camHistoOriginal = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\histograma.png";
			//Funcao substituirTexto
			arq = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\classificacao.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\funcoes\\classificarImagem.p",
	      		      "--img",
	      		      "",
	      		      "--pc",
	      		      ""
    		    };
			cmdExecEntrada = entrada;
			
			String[] filtro = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\funcoes\\filtro.py",
	      		      "--img",
	      		      "",
	      		      "--pc",
	      		      "",
	      		      "--problema",
	      		      "1"
  		    };
			cmdExecFiltro = filtro;
			camImagemEditada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\imgFiltrada.png";
			
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens");	//pc pessoal
			
		}else { //projeto
			camHistoOriginal = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\histograma.png";
			//Funcao substituirTexto
			arq = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\classificacao.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
      		      "python",
      		      "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\funcoes\\classificarImagem.py",
      		      "--img",
      		      "",
      		      "--pc",
    		      "",
      		};
			cmdExecEntrada = entrada;
			
			String[] filtro = {
	      		      "python",
	      		      "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\funcoes\\filtro.py",
	      		      "--img",
	      		      "",
	      		      "--pc",
	      		      "",
	      		      "--problema",
	      		      "1"
		    };
			cmdExecFiltro = filtro;
			camImagemEditada = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\imgFiltrada.png";
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\1imagensEntrada");	//pc Projeto
		}

	}
	
	public void ExecutarScriptPython(String img, String pc) {
        try {
        	cmdExecEntrada[3] = img; 
        	cmdExecEntrada[5] = pc; 
		    Runtime.getRuntime().exec(cmdExecEntrada);
		    
		    Thread.sleep(2200);

        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	public void ExeScriptPythonFiltro(String saida, String pc, String problema) {
        try {
        	cmdExecFiltro[3] = saida; 
        	cmdExecFiltro[5] = pc; 
        	//cmdExecEntrada[7] = problema; 
        	
		    Runtime.getRuntime().exec(cmdExecFiltro);
		    Thread.sleep(3200);
		    //verificarSaida();

        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	
}

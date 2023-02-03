package interfaceJava;

import java.awt.Button;
import java.awt.Label;
import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

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
	public String camHistoOriginal;
	public String camImagem;
	public String camImagemEditada;
	
	public void definirDiretorios(String i) {
		
		if( i == "0" ) {//pessoal
			camHistoOriginal = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.png";
			//Funcao substituirTexto
			arq = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\saida.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\main.py",
	      		      "--img",
	      		      "",
	      		      "--pc",
	      		      ""
    		    };
			cmdExecEntrada = entrada;
			
			String[] filtro = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\filtro.py",
	      		      "--img",
	      		      "",
	      		      "--pc",
	      		      "",
	      		      "--problema",
	      		      ""
  		    };
			cmdExecFiltro = filtro;
			camImagemEditada = "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\saidas\\imgFiltrada.png";
			
			//Funcao btnEsq.addActionListener
			jfc = new JFileChooser("H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\imagens");	//pc pessoal
			
		}else { //projeto
			//Funcao substituirImagem
			camHistoOriginal = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.png";
			//Funcao substituirTexto
			arq = "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\saidas\\saida.txt";
			//Funcao ExecutarScriptPython
			String[] entrada = {
      		      "python",
      		      "C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\main.py",
      		      "--img",
      		      "",
      		      "--pc",
    		      ""
      		    };
			cmdExecEntrada = entrada;
			
			String[] filtro = {
	      		      "python",
	      		      "H:\\SmithHD\\Documentos\\4-github\\AppArtigo\\python\\filtro.py",
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
			jfc = new JFileChooser("C:\\Users\\Smith Fernandes\\Documents\\4 - github\\AppArtigo\\python\\imagens");	//pc Projeto
		}

	}
	
	public void ExecutarScriptPython(String saida, String pc) {
        try {
        	cmdExecEntrada[3] = saida; 
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
        	cmdExecEntrada[5] = pc; 
        	//cmdExecEntrada[7] = problema; 
		    Runtime.getRuntime().exec(cmdExecFiltro);
		    
		    Thread.sleep(2200);

        } catch(Exception e) {
            System.err.println(e);
        }
	}
	
	
}

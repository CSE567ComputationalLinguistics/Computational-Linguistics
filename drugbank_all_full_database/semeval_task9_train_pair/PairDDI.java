import java.io.*;
import java.util.StringTokenizer;
import java.util.Hashtable;
import java.util.zip.GZIPInputStream;


public class PairDDI {

	public static void main (String[] args) throws IOException {

		String fileName = args[0];
		//	BufferedReader d = new BufferedReader(new InputStreamReader(new FileInputStream(new File (fileName))));
		//                OutputStreamWriter out = new OutputStreamWriter (new FileOutputStream(fileName+".1"), "UTF-8");
		BufferedReader d;
		if (fileName.endsWith(".gz")) {
			d = new BufferedReader(new InputStreamReader(new GZIPInputStream(new FileInputStream(new File(fileName)))));
		}
		else {
			d = new BufferedReader(new InputStreamReader(new FileInputStream(new File(fileName))));
		}
		String str = new String();
		str = d.readLine();

		while (str != null) {
			str = str.trim();

			String delim = "<";
			Hashtable  hash = new Hashtable(); 
			StringTokenizer st = new StringTokenizer(str, delim, true);
			while (st.hasMoreTokens()) {
				String tok = st.nextToken();
				if (tok.startsWith("sentence id") || 
						tok.startsWith("entity id") || tok.startsWith("pair id")  || tok.startsWith("/sentence>")) {
					String delim2 = " ";
					String[] entry;
					entry = tok.split(delim2);
					for(int i=0; i<entry.length; i++) {
						String token = entry[i];
						if (token.contains("=") && !token.contains("text=")) {
							token = token.substring(token.indexOf("\"")+1, token.lastIndexOf("\"")).trim();
							System.out.println(token); 
							entry[i] = token; 
						}
						else if (token.contains("text=")) break;
					}

					String id = new String(); 
					String type = new String(); 
					String text = new String(); 
					String e1 = new String(); 
					String e2 = new String(); 
					String interaction = new String(); 

					if (tok.startsWith("sentence id")) { 
						hash = new Hashtable(); 
					}
					else if (tok.startsWith("entity id")) {id = entry[1]; type = entry[4];    
						text = tok.substring(tok.indexOf("text="), tok.lastIndexOf("\"")).trim(); 
						text = text.substring(text.indexOf("\"")+1, text.length()).trim(); 
						hash.put(id, text); 

					}
					else if (tok.startsWith("pair id")) { id = entry[1];  e1 = entry[2]; e2 = entry[3]; interaction = entry[4];
						//System.out.println(id); 
						System.out.println(e1 + ":" + hash.get(e1) +"\t" + e2 + ":" + hash.get(e2) + "\t" + interaction); ; 

					}
					else if (tok.startsWith("/sentence>")) {


					}
				}


			}


			str = d.readLine();
		}
		d.close();
	}
}

/*
   StringTokenizer st = new StringTokenizer(str, delim);
   while (st.hasMoreTokens()) {
   String tok = st.nextToken();
   }
 */
/*
   Enumeration k = hash.keys();
   while(k.hasMoreElements()) {
   String key = (String) k.nextElement();
   System.out.println(key + "\t" + hash.get(key));
   }
 */

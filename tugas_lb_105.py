import time
import random

def simulasi_beban_dinamis_152024105():
    # Inisialisasi daftar pekerjaan (tasks)
    antrian_tugas = [f"Task_ID_{i}" for i in range(1, 16)]
    
    # Status beban kerja pada dua pemroses (Node)
    # Dimulai dari 0 (masih kosong)
    status_node = {
        "Node_Primer": 0,
        "Node_Sekunder": 0
    }
    
    start_point = time.perf_counter()
    
    print("--- [SISTEM DIMULAI: DYNAMIC LOAD BALANCING] ---")
    print(f"NRP: 152024105 | Mode: Distribusi Dinamis\n")

    for tugas in antrian_tugas:
        # LOGIKA DINAMIS: Mencari node dengan beban paling rendah saat ini
        # Ini adalah inti dari Dynamic Distribution
        node_target = min(status_node, key=status_node.get)
        
        # Simulasi beban kerja acak (workload effort)
        effort = random.uniform(0.1, 0.5) 
        status_node[node_target] += 1
        
        print(f"[LOG] {tugas} dialokasikan ke {node_target} (Beban: {status_node[node_target]})")
        
        # Simulasi pengerjaan oleh CPU
        time.sleep(effort)
        
    end_point = time.perf_counter()
    waktu_optimal = end_point - start_point
    
    print("\n" + "="*50)
    print("REKAPITULASI PEMBAGIAN BEBAN")
    print("="*50)
    for node, total in status_node.items():
        print(f"> {node} memproses total: {total} tugas")
    
    # Poin penting tugas: Menunjukkan Expected Optimal Time
    print(f"\n[HASIL] Expected Optimal Time Tercapai: {waktu_optimal:.4f} detik")
    print("="*50)

if __name__ == "__main__":
    simulasi_beban_dinamis_152024105()
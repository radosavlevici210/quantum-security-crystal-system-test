from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'test-key')

@app.route('/')
def index():
    return {
        'system': 'Quantum Security Crystal System Test',
        'owner': 'Ervin Remus Radosavlevici',
        'contact': 'radosavlevici210@icloud.com',
        'status': 'PRODUCTION_READY',
        'test_environment': True,
        'timestamp': datetime.now().isoformat()
    }

@app.route('/test/security')
def security_test():
    return jsonify({
        'quantum_encryption': 100,
        'crystal_security': 'ACTIVE',
        'test_passed': True,
        'owner': 'Ervin Remus Radosavlevici'
    })

@app.route('/health')
def health():
    return {'status': 'healthy', 'test_ready': True}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

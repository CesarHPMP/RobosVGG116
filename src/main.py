import tensorflow as tf
from tf_keras.applications import VGG16
from tf_keras.layers import Dense, GlobalAveragePooling2D
from tf_keras.models import Model
from tf_keras.preprocessing.image import ImageDataGenerator
from tf_keras.optimizers import Adam
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Configurações básicas
img_height, img_width = 224, 224
batch_size = 5
num_classes = 2  # Altere para o número de classes no seu conjunto de dados

# Caminhos para os diretórios dos dados


train_data_dir = '../data'
validation_data_dir = '../valid_data'
test_data_dir = '../test_data'

# Carregar o modelo VGG16 sem as camadas de topo
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))

# Congelar as camadas da base VGG16
for layer in base_model.layers:
    layer.trainable = False

# Adicionar camadas customizadas
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
x = Dense(512, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

# Criar o modelo completo
model = Model(inputs=base_model.input, outputs=predictions)

# Compilar o modelo
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Preparação dos dados usando ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1.0/255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1.0/255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

# Treinamento do modelo
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=10
)

# Avaliação do modelo
test_generator = test_datagen.flow_from_directory(
    test_data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical'
)

loss, accuracy = model.evaluate(test_generator)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
